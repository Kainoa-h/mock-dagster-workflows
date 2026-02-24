{
  description = "Python 3.11 development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python311;
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python
          ];

          # Optional: Add any other system dependencies here
          packages = with pkgs; [
            # git
            # libffi
            # openssl
          ];

          shellHook = ''
            echo "Python 3.11 development environment loaded"
          '';
        };
      }
    );
}
