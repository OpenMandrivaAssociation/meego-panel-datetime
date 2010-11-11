Name: meego-panel-datetime
Version: 0.3.2
Release: %mkrel 1
Summary: Date/Time panel
License: GPL v2 or later
Source: meego-panel-datetime-0.3.2.tar.gz
Patch1: fix-desktop-file.patch
Group: System/Desktop
BuildRequires: intltool >= 0.35.5
BuildRequires: libGConf2-devel
BuildRequires: libnotify-devel
BuildRequires: libcanberra-devel
BuildRequires: libgweather-devel
BuildRequires: libpenge-devel
BuildRequires: jana-devel
BuildRequires: gettext
BuildRequires: glib2-devel >= 2.16.1
BuildRequires: mx-devel
BuildRequires: meego-panel-devel
Obsoletes: moblin-panel-datetime < 0.3.2

%description
Date and Time panel which features world clock and alarm support.

%prep
%setup -q
%patch1 -p1 -b .fix-desktop-file

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf %buildroot

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/date-time.schemas > /dev/null

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/gconf/schemas/date-time.schemas
%{_libdir}/*
%{_datadir}/*
