{
  description = "Minimal Nix Shell with Bash";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    nixpkgs.inputs = {};
  };

  outputs = { self, nixpkgs }: {
      packages.x86_64-linux.default =
        with import nixpkgs { system = "x86_64-linux"; };
        pkgs.mkShell {
            buildInputs = with import nixpkgs { system = "x86_64-linux"; }; [
                zellij
                fsearch
                bash
            ];
    };
  };
}