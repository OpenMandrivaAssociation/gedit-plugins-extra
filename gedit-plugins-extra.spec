%define name gedit-plugins-extra
%define version 2.24.1
%define release %mkrel 7

Summary: Unofficial set of plugins for gedit
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.nanolx.org/free/%{name}-%{version}.tar.bz2
Source1: http://sourceforge.net/projects/gedit-latex/files/Gedit%20LaTeX%20Plugin/0.2/LaTeXPlugin-0.2.tar.gz
#gw the COPYING is v3, but the comments say v2+
License: GPLv2+
Group: Editors
#Url: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gedit-devel
BuildRequires: python-gtksourceview-devel
BuildRequires: ctags
BuildRequires: gnome-vfs2-devel
BuildRequires: libglade2.0-devel
Requires: gedit
Requires: python-gtksourceview
Requires: gnome-python-gnomevfs
Requires: gnome-python-gtkmozembed
Requires: pygtk2.0-libglade
Requires: ctags
#gw latex plugin, bug #56261
Requires: rubber

%description
gEdit is a small but powerful text editor designed expressly
for GNOME.

This package contains some thirdparty plugins for gEdit, extending gEdit
functionality.

%prep
%setup -q -n %name -a 1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %buildroot%_libdir/gedit-2/plugins/LaTeXPlugin*
cp -rf GeditLaTeXPlugin* %buildroot%_libdir/gedit-2/plugins/
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS AUTHORS  ChangeLog README NEWS
%_libdir/gedit-2/plugins/*
%_datadir/gtksourceview-2.0/styles/*.xml
%_libdir/pkgconfig/*.pc
