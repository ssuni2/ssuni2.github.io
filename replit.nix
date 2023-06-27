{ pkgs }: {
  deps = [
    pkgs.python38Packages.pip
    pkgs.python39Packages.pip
    pkgs.qtile
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}