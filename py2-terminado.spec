### RPM external py2-terminado 0.8.1
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}
## INITENV +PATH PYTHON3PATH %{i}/${PYTHON3_LIB_SITE_PACKAGES}


%define pip_name terminado
Requires: py2-backports py2-ordereddict py2-tornado py2-six py2-ptyprocess  py2-singledispatch py2-certifi 

## IMPORT build-with-pip

