%define module    qtpy
%define pypi_name QtPy

Name:           python-%{module}
Version:        2.4.3
Release:        1
Summary:        Abstraction layer for PyQt5/PyQt4/PySide
Group:          Development/Python
License:        MIT and BSD
URL:            https://github.com/spyder-ide/qtpy
Source0:        https://github.com/spyder-ide/%{module}/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{module}}

%description
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
%py_build

%install
%py_install

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/qtpy
%{python_sitelib}/%{module}
%{python_sitelib}/QtPy-%{version}.dist-info/
