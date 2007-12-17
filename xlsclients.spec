Name:		xlsclients
Version:	1.0.1
Release:	%mkrel 4
Summary:	List client applications running on a display
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxmu-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xlsclients is a utility for listing information about the client
applications running on a display. It may be used to generate scripts
representing a snapshot of the user's current session.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xlsclients
%{_mandir}/man1/xlsclients.1*

