%define name gedit-plugins-extra
%define version 2.24.1
%define release %mkrel 1

Summary: Unofficial set of plugins for gedit
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.nanolx.org/free/%{name}-%{version}.tar.bz2
#gw the COPYING is v3, but the comments say v2+
License: GPLv2+
Group: Editors
#Url: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gedit-devel
BuildRequires: python-gtksourceview-devel
BuildRequires: ctags
BuildRequires: libgnome-vfs2-devel
BuildRequires: libglade2.0-devel
Requires: gedit
Requires: python-gtksourceview
Requires: gnome-python-gnomevfs
Requires: pygtk2.0-libglade
Requires: ctags

%description
gEdit is a small but powerful text editor designed expressly
for GNOME.

This package contains some thirdparty plugins for gEdit, extending gEdit
functionality.

%prep
%setup -q -n %name

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS AUTHORS  ChangeLog README NEWS
%_libdir/gedit-2/plugins/*
%_datadir/gtksourceview-2.0/styles/*.xml
%_libdir/pkgconfig/*.pc
