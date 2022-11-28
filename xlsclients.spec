Name:		xlsclients
Version:	1.1.5
Release:	1
Summary:	List client applications running on a display
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb)

%description
Xlsclients is a utility for listing information about the client
applications running on a display. It may be used to generate scripts
representing a snapshot of the user's current session.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xlsclients
%doc %{_mandir}/man1/xlsclients.1*
