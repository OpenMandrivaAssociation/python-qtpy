%define module    qtpy
%define pypi_name QtPy

Name:           python-%{module}
Version:        1.11.0
Release:        1
Summary:        Abstraction layer for PyQt5/PyQt4/PySide (Python 2)
Group:          Development/Python
License:        MIT and BSD
URL:            https://github.com/spyder-ide/qtpy
Source0:        https://github.com/spyder-ide/%{module}/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

%description
QtPy (pronounced ‘cutie pie’) is a small abstraction layer that lets
you write applications using a single API call to either PyQt or
PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import
qt from qtpy instead of PyQt5.

#----------------------------------------------------

%package -n     python3-%{module}
Summary:        Abstraction layer for PyQt5/PyQt4/PySide (Python 3)
Group:          Development/Python
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{module}}

%description -n python3-%{module}
QtPy (pronounced ‘cutie pie’) is a small abstraction layer that lets
you write applications using a single API call to either PyQt or
PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import
qt from qtpy instead of PyQt5.

#----------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
