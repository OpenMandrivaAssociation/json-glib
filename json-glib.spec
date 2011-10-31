%define libver		1.0
%define major		0
%define girmajor	1.0

%define libname		%mklibname %{name} %{libver} %{major}
%define develname	%mklibname %{name} -d
%define girname		%mklibname %{name}-gir %{girmajor}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		json-glib
Version:	0.14.2
Release:	1
Summary:	Library for JavaScript Object Notation format
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/JsonGlib
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
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
Requires:	%{name} = %{version}

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

%package -n %{girname}
Summary:        GObject Introspection interface description for %name
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Conflicts:	%{mklibname %{name}1.0-gir 1.0} < 0.13.4-3

%description -n %{girname}
GObject Introspection interface description for %name.

%prep
%setup -q

%build
%configure2_5x	--disable-static
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name}-%{libver}

%check
%make check

%clean
rm -rf %{buildroot}

%files -f %{name}-%{libver}.lang

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib%{name}-%{libver}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Json-%{girmajor}.typelib

%files -n %{develname}
%defattr(-,root,root,-)
%doc README NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/lib%{name}-%{libver}.so
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_includedir}/%{name}-%{libver}/
%{_datadir}/gir-1.0/Json-%{girmajor}.gir
