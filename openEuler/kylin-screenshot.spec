%define debug_package %{nil}
Name:           kylin-screenshot
Version:        1.0.0
Release:        1
Summary:        a powerful screenshot and screen recording tool
License:        GPL-3+
URL:            https://github.com/ubuntukylin
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtx11extras
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXinerama
BuildRequires:  libXfixes-devel
BuildRequires:  libXfixes
BuildRequires:  libX11-devel
# BuildRequires:  ffmpeg-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kwindowsystem
BuildRequires:  gsettings-qt-devel

# Requires: NetworkManager

%description
 Powerful yet simple-to-use screenshot software
 kylin-screenshot is a powerful screenshot and screen recording tool.
 It allows you to take screenshots of the captured images in rectangular
 and circular boxes, set blur, add markers, add text and more. And set
 mouse display, sound recording, video frame rate, audio bit rate when
 making screen recording.

%prep
%setup -q

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-screenshot.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/kylin-screenshot
%{_datadir}/applications/kylin-screenshot.desktop
%{_datadir}/dbus-1/interfaces/org.dharkael.kylinscreenshot.xml
%{_datadir}/dbus-1/services/org.dharkael.kylinscreenshot.service
%{_datadir}/glib-2.0/schemas/org.ukui.screenshot.gschema.xml
%{_datadir}/icons/hicolor/128x128/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/128x128@2x/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/16x16/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/16x16@2x/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/24x24/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/256x256/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/256x256@2x/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/32x32/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/32x32@2x/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/48x48/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/48x48@2x/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/64x64@2x/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/96x96/apps/kylin-screenshot.png
%{_datadir}/icons/hicolor/96x96@2x/apps/kylin-screenshot.png
%{_datadir}/kylin-screenshot/translations/Internationalization_ca.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_de_DE.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_es.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_fr.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_ja.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_ka.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_pl.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_pt_br.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_ru.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_sk.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_sr.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_tr.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_uk.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_zh_CN.qm
%{_datadir}/kylin-screenshot/translations/Internationalization_zh_TW.qm
%{_datadir}/metainfo/kylinscreenshot.appdata.xml

%changelog
* Tue Dec 15 2020 lvhan <lvhan@kylinos.cn> - 1.0.0-1
- update to upstream version 1.0.0-1
