Name:		xlsclients
Version:	1.1.4
Release:	2
Summary:	List client applications running on a display
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb)
BuildRequires: x11-util-macros >= 1.0.1

%description
Xlsclients is a utility for listing information about the client
applications running on a display. It may be used to generate scripts
representing a snapshot of the user's current session.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xlsclients
%{_mandir}/man1/xlsclients.1*


%changelog
* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-1mdv2012.0
+ Revision: 699286
- update to new version 1.1.2

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 671338
- mass rebuild

* Sun Sep 26 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 581089
- new release

* Thu Jul 22 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2011.0
+ Revision: 557060
- New version: 1.1.0

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 464735
- New version: 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 350989
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226057
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154431
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 76541
- rebuild for 2008
- add description
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

