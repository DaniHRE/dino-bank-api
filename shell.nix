with import <nixpkgs> {};

pkgs.mkShell {
  buildInputs = [
    python310Packages.django
    python310Packages.djangorestframework
  ];
}
