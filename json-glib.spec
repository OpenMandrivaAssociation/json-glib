%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname %{name} -d

Summary:	Library for JavaScript Object Notation format
Name:		json-glib
Version:	1.1.2
Release:	0.1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://live.gnome.org/JsonGlib
Source0:	http://ftp.gnome.org/pub/GNOME/sources/json-glib/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

Obsoletes:	 json-glib-i18n < 1.1.2
Provides:	 json-glib-i18n = 1.1.2

%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}json-glib1.0_0 < 0.15.2-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

%check
%make check

%files -f %{name}-%{api}.lang
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_mandir}/man1/json-glib-*.1.*

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%_libdir/girepository-1.0/Json-%{api}.typelib

%files -n %{devname}
%doc NEWS ChangeLog
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/%{name}-%{api}/
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Json-%{api}.gir

