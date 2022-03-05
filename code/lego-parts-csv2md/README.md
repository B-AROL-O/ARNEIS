# LEGO&reg; Partlists CSV to MD converter

This tool is used to create a Markdown part list from a BOM (Bill Of Materials) as
exported to CSV file from [Stud.IO CAD](https://www.bricklink.com/v3/studio/download.page).

The tool is written in a Python [Jupyther Notebook](https://jupyter.org) and can be run directly inside [Visual Studio Code](https://code.visualstudio.com).

## Python environment
Obviously you need to have `python3` installed on your system. In case you haven't it you can follow instructions from [python.org](https://www.python.org) or any tutorial you can find in internet.

Since this tool need some libraries I suggest you to create a [virtual environment](https://docs.python.org/3/library/venv.html) where to install those libraries keeping your system clean.

### Creating virtual environment

To create a _virtual environment_ in the folder you are in, use the following command in your command console
``` (sh)
python3 -m venv env
```
this will create a `env` folder where all the Python libraries will be installed.

### Activate the virtual environment

> **NOTE**
>
> If you use _Visual Studio Code_ to run the Python Jupyter Notebook you do not need to activate the environment since it will be automatically used by VSC


Once created the virtualenvironment need to be activated in order to be used.
Depending on your Operating System to activate the environment follow the command shown in following table

| Platform | Shell | Command to activate virtual environment |
| -------- | ----- | --------------------------------------- |
| POSIX    | bash/zsh | `$ source env/bin/activate` |
|          | fish | `$ source env/bin/activate.fish` |
|          | csh/tsch | `$ source env/bin/activate.csh` |
|          | PowerShell Core | `$ env/bin/Activate.ps1` |
| Windows  | cmd.exe | `C:\> env\Scripts\activate.bat` |
|          | PowerShell | `PS C:\> env\Scripts\Activate.ps1` |

### Deactivate the virtual environment

You can simply deactivate an active _virtual environment_ by using the command

```console
deactivate
```
## Using VSC (Visual Studio Code)

The `partlist-csv2md.ipynb` file is developed to be used inside Visual Studio Code.

Open the file inside the editor.

> If it is the first time you open a Python source or a Jupyter Notebook
> then VSC will propose you
> to install proper extensions.
>
> **Accept the automatic installation of all extensions**

### Select the _Python kernel_

In the up-right corner of the opened editor use the `Select Kernel` menu and choose the python executable VSC will use to run the app. In case you did the _virtual environment_ job, be sure to choose this as your kernel

### Test that all is working

Press the `Run All` menu voice and wait...

> **ATTENTION**
>
> The first time you try to run app, VSC will ask to install other needed libraries.
> In particular it need to install `ipykernel` to be able to run your _Jupyther Notebook_ app.
>
> **Accept the automatic installation of all extensions**
>
> After all installations are done you need to press again `Run All`

The first time you run this app some more libraries are automatically imported so, only on the first run, you need to wait more time.

If all is working you will see a table list converted from the `test.csv` demo file.

## Use it for your own conversions

From now on you can use this Notebook to convert your LEGO&reg; part list to beautifull documents.

