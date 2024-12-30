{
  description = "An implementation of ontology logs";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        py = pkgs.python310.withPackages (ps: with ps; [
          click-repl
          jsonschema
        ]);
        zatske = pkgs.stdenv.mkDerivation {
          name = "zatske";
          version = "0.0.1";

          src = ./.;

          buildPhase = ''
            echo "#!${py}/bin/python" > shebang
            sed -i -e 's,@SCHEMA@,${./schema.json},' zatske.py
          '';

          installPhase = ''
            mkdir -p $out/bin/
            cat shebang zatske.py > $out/bin/zatske
            chmod +x $out/bin/zatske

            mkdir -p $out/share/
            cp schema.json $out/share/
          '';
        };
      in {
        packages = {
          default = zatske;
        };
        devShells.default = pkgs.mkShell {
          name = "zatske-env";
          packages = [ pkgs.jq py ];
        };
      }
    );
}
