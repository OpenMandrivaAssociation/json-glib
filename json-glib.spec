%define libver 1.0
%define major 0

%define libname		%mklibname %{name} %{libver} %{major}
%define develname	%mklibname %{name} -d

Name:		json-glib
Version:	0.14.2
Release:	4
Summary:	Library for JavaScript Object Notation format
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/JsonGlib
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gtk-doc
Requires:	%{libname} = %{version}-%{release}

%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.


%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x	--disable-static
%make 


%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}-%{libver}

%check
%make check

%files -f %{name}-%{libver}.lang

%files -n %{libname}
%{_libdir}/lib%{name}-%{libver}.so.%{major}*
%_libdir/girepository-1.0/Json-%{libver}.typelib

%files -n %{develname}
%doc README NEWS ChangeLog
%{_libdir}/lib%{name}-%{libver}.so
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_includedir}/%{name}-%{libver}/
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Json-%{libver}.gir


%changelog
* Mon Aug 20 2012 Arkady L. Shane <ashejn@@rosalab.ru> 0.14.2-2
- drop la files

* Sat Jun 23 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.14.2-1
- Update to 0.14.2

* Wed Jun 15 2011 Götz Waschk <waschk@mandriva.org> 0.12.6-1mdv2011.0
+ Revision: 685394
- new version
- xz tarball

* Tue Apr 12 2011 Götz Waschk <waschk@mandriva.org> 0.12.4-1
+ Revision: 652810
- update to new version 0.12.4

* Mon Jan 10 2011 Götz Waschk <waschk@mandriva.org> 0.12.2-1
+ Revision: 630851
- new version

* Sat Sep 25 2010 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2011.0
+ Revision: 580982
- update to new version 0.12.0

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 0.11.2-2mdv2011.0
+ Revision: 577921
- rebuild for new g-i

* Mon Aug 02 2010 Götz Waschk <waschk@mandriva.org> 0.11.2-1mdv2011.0
+ Revision: 565071
- new version
- drop patch

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.10.4-2mdv2011.0
+ Revision: 563323
- rebuild for new gobject-introspection

* Fri Mar 19 2010 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2010.1
+ Revision: 525304
- update to new version 0.10.4

  + Anssi Hannula <anssi@mandriva.org>
    - fix hardcoded paths in pkgconfig file (reported by Juho Teperi)

* Fri Feb 26 2010 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2010.1
+ Revision: 511958
- new version

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 0.10.0-2mdv2010.1
+ Revision: 486165
- enable introspection
- fix devel provides
- readd libtool archive

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 483944
- update to new version 0.10.0

* Thu Dec 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 476181
- Update to new version 0.9.2
- Update to new version 0.8.2

* Mon Sep 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2010.0
+ Revision: 450642
- Update to new version 0.8.0

* Wed Sep 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.6-1mdv2010.0
+ Revision: 435924
- Update to new version 0.7.6

* Wed Aug 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.4-1mdv2010.0
+ Revision: 415768
- Update to new version 0.7.4
- Run test suite

* Fri Jul 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 394336
- BuildRequires: gtk-doc
- Disable gobject-introspection again: probably needs some more work
  to correctly package this
- BuildRequires: gobject-introspection
- commit first SPEC file, based on Fedora's
- Don't run test suite, it sometimes hangs
- create json-glib

