{
  description = "Minimal Nix Shell with Bash";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    nixpkgs.inputs = {};
  };

  outputs = { self, nixpkgs }: {
    nixConfigurations = {
      default = {
        packages = [ nixpkgs.bash ];
      };
    };
  };
}
