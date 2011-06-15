%define libver 1.0
%define major 0

%define libname		%mklibname %{name} %{libver} %{major}
%define develname	%mklibname %{name} -d

Name:		json-glib
Version:	0.12.6
Release:	%mkrel 1
Summary:	Library for JavaScript Object Notation format
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/JsonGlib
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
Requires:	%{libname} = %{version}

%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}
Provides:	lib%%{name} = %{version}

%description -n %{libname}
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.


%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	lib%{name}-devel = %version-%release
Requires:	%{libname} = %{version}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x	--enable-static=no
%make 


%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make check

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib%{name}-%{libver}.so.%{major}*
%_libdir/girepository-1.0/Json-%{libver}.typelib

%files -n %{develname}
%defattr(-,root,root,-)
%doc README NEWS ChangeLog
%{_libdir}/lib%{name}-%{libver}.la
%{_libdir}/lib%{name}-%{libver}.so
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_includedir}/%{name}-%{libver}/
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Json-%{libver}.gir
