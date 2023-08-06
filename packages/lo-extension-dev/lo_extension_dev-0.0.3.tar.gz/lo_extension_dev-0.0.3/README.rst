=============================
Libreoffice Developing Helper
=============================


This tool helps developing LibreOffice Extension. It mainly does:

    - build an LibreOffice extension from your source

    - create the `Addons.xcu` file following a simple yaml conf file.

    - install / uninstall extension

    - create shortcut from installed extension to development files

WHY
---
When developing for LibreOffice, it is common to often reinstall the extension
to test it. It means compiling, uninstalling, installing. This tasks are time
consuming. Beside, if you want to make modification of your code without
reinstalling, you need to create some shortcuts from the installation path to
your code. This command line tool helps achieving this goal.


Installation
------------

::

  $ pip install lo-extension-dev

Then create two config files using yaml. One to configure your extension, the
other one to create the `Addons.xcu` files (OfficeMenuBar & OfficeToolBar).


Usage
-----

To develop a LibreOffice extension, we advocate to use the following
architecture. Your extension code is in `src/`.

::

    ─ my_extension
        │   ├── addons_conf.yml
    │   ├── Addons.xcu
    │   ├── extension
    │   │   ├── 0.0.1
    │   │   │   ├── lo-extension-testing.oxt
    │   ├── extension.yml
    │   ├── README.md
    │   └── src
    │       ├── Accelerators.xcu
    │       ├── Addons.xcu
    │       ├── assets
    │       │   ├── avaudiologo.svg
    │       │   └── sc_underline.svg
    │       ├── description
    │       │   ├── descr-en.txt
    │       ├── description.xml
    │       ├── dialogs
    │       │   ├── window.xdl
    │       ├── Events.xcu
    │       ├── META-INF
    │       │   └── manifest.xml
    │       ├── Office
    │       │   └── UI
    │       ├── python
    │       │   ├── pythonpath
    │       │   └── my_macros.py
    │       ├── README.md
    │       └── registration
    │           ├── license_en.txt
    └── README.md

Once installed, a functino `manage_extension` is available in your terminal.

To get help, just type:

    $ manage_extension -h


    options:
      -h, --help          show this help message and exit
      -o, --open          Open installation directory
      -m, --make          Make extension
      -i, --install       Install extension
      -u, --uninstall     Uninstall extension
      -d, --dev           Set dev shortcuts
      -id, --install-dev  Install and set dev shortcuts


Configuration files
-------------------

We use two configuration files, using `yaml` syntax. One to generate menubar
menu and toolbar menu. The second one hold the extension configuration.

extension.yml
~~~~~~~~~~~~~
- version : version number in format 0.0.1

- extension_name : name of your extension (no space)

- file_extension : zip or oxt

- lib : com.company.my_extension

- macros_directory : in this example, it is `python`. In some project, it is `macros`.

-addons_conf : it shouldn't be changed. The file holding menubar & toolbar conf.

- menu_name : the label displayed in the menu bar.


addons_conf.yml
~~~~~~~~~~~~~~~
This files has two main sections :

- OfficeMenuBar

- OfficeToolBar

You can create a `submenu`. Don't forget, the keys following a submenu have to
be named as the function they call. It's the same logic for the OfficeToolBar.



