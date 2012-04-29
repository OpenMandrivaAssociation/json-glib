%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define api		1.0
%define major		0
%define girmajor	1.0

%define libname		%mklibname %{name} %{api} %{major}
%define develname	%mklibname %{name} -d
%define girname		%mklibname %{name}-gir %{girmajor}

Summary:	Library for JavaScript Object Notation format
Name:		json-glib
Version:	0.14.2
Release:	2
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/JsonGlib
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Suggests:	%{name} = %{version}

%description -n %{libname}
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Conflicts:	%{mklibname %{name}1.0-gir 1.0} < 0.13.4-3

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x	--disable-static
%make 

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name}-%{api}

%check
%make check

%files -f %{name}-%{api}.lang

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Json-%{girmajor}.typelib

%files -n %{develname}
%doc README NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/%{name}-%{api}/
%{_datadir}/gir-1.0/Json-%{girmajor}.gir

