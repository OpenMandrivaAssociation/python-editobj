%define	oname	Editobj3
%global module	%(echo %oname | tr [:upper:] [:lower:])
%global mod		%(m=%{oname}; echo ${m:0:1})

Summary: 	An automatic dialog box generator for Python objects
Name: 	 	python-%{module}
Version: 	0.2
Release: 	1
License:	GPLv2
Group:		Development/Python
Source0:	https://pypi.io/packages/source/%{mod}/%{oname}/%{oname}-%{version}.tar.gz
URL:		https://home.gna.org/oomadness/en/editobj/

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

#Obsoletes:	editobj
BuildArch:	noarch

%rename		python-editobj

%description
Editobj3 is an automatic dialog box generator for Python objects. It supports
several backends; currenlty Qt, GTK and HTML are supported. The HTML backend
is based on W2UI, and can be used either in local single user mode, or in
distributed multiple users mode.

Editobj3 dialog boxes are composed of an attribute list, a luxurious
good-looking but useless icon and title bar, and a tree view (if the edited
object is part of a tree-like structure). Editobj3 includes an advanced
introspection module that usually guesses how to edit any object; it can also
be customized for a given class of object through the editobj3.introsp module.
Editobj3 also supports the simultaneous edition of a group of objects, as if
they were a single object.

%files
%license LICENSE.txt
%doc README.rst
%{py_puresitedir}/%{module}
%{py_puresitedir}/*.egg-info

#-----------------------------------------------------------------------

%prep
%autosetup -n %{oname}-%{version}

%build
%py_build

%install
%py_install

