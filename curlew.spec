%global commit 10aa181c3839a3ec31faea849ed02fac0a5f9d91
Name:       curlew
Version:    0.2.5
Release:    1%{?dist}
Summary:    Multimedia converter
License:    Waqf
URL:        https://github.com/chamfay/Curlew
Source0:    %{url}/archive/%{commit}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  librsvg2-tools
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools

Requires:   ffmpeg
Requires:   gstreamer1
Requires:   gtk3
Requires:   hicolor-icon-theme
Requires:   mediainfo
Requires:   python3
%if 0%{?fedora} < 33
Requires:   python3-configparser
%endif
Requires:   python3-dbus
Requires:   python3-gobject
Requires:   xdg-utils


%description
Easy to use, Free and Open-Source Multimedia converter for Linux.
Curlew written in python and GTK3 and it depends on (ffmpeg/avconv).

%prep
%autosetup -n Curlew-%{commit}

%build
%{py3_build}

%install
%{py3_install}
rm -rf %{buildroot}%{_datadir}/doc/

desktop-file-edit --remove-key=Encoding %{buildroot}%{_datadir}/applications/curlew.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/curlew.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README THANKS TODO
%license LICENSE-en.txt LICENSE-ar.txt
%{_bindir}/curlew
%{python3_sitelib}/curlew-*-py%{python3_version}.egg-info
%{_datadir}/applications/curlew.desktop
%dir %{_datadir}/curlew/
%{_datadir}/curlew/modules
%{_datadir}/curlew/done.ogg
%{_datadir}/curlew/formats.cfg
%{_datadir}/icons/hicolor/*/apps/curlew.*
%{_datadir}/pixmaps/curlew.svg


%changelog
* Thu Nov 18 2021 Sérgio Basto <sergio@serjux.com> - 0.2.5-1
- Update curlew to 0.2.5

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.4-8
- Rebuild for python-3.10

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 0.2.4-5
- Rebuild for python-3.9

* Sun May 24 2020 Leigh Scott <leigh123linux@gmail.com> - 0.2.4-4
- Fix F33 requires, python3-configparser in part of python3

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Leigh Scott <leigh123linux@gmail.com> - 0.2.4-2
- Review changes to fix lang and desktop file issues

* Mon Jan 06 2020 Leigh Scott <leigh123linux@gmail.com> - 0.2.4-1
- Initial build

