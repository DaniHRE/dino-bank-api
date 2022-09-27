{ pkgs ? import <nixpkgs> {} }: with pkgs;

mkShell {
  buildInputs = [
    python310Packages.django
    python310Packages.djangorestframework
  ];
}