Summary:	Guitar Pro 6
Name:		guitar-pro
Version:	6
Release:	0.5
License:	Proprietary (not redistributable)
Group:		Applications/Multimedia
# Source0Download: http://www.guitar-pro.com/en/index.php?pg=download
Source0:	http://download3.guitar-pro.com/gp6/gp%{version}-full-linux-demo-r11621.deb
# NoSource0-md5:	57afc9199affe93952d38a05600b54e0
NoSource:	0
URL:		http://www.guitar-pro.com/en/index.php?pg=product
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	%{name}-data = %{version}
Requires:	desktop-file-utils
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{_prefix}/lib/%{name}
%define		_enable_debug_packages	0

%define		_noautoprovfiles	%{_appdir}

# we don't want these to be provided as system libraries
# to update, 'rpm -q --provides' should be empty
%define		libs1		libGPCore.so libOverLoud.so libPickupModeling.so libRSEAudioCore.so libRSECore.so libWavFile.so libZip.so
%define		libs2		libchunk.so libexception.so libfactory.so libfilesystem.so libmemory.so libmmap.so libobject.so libregister.so libthread.so libtimer.so libvariant.so libxml.so libprofiler.so
%define		qt_libs		libQtCore.so.4 libQtDBus.so.4 libQtGui.so.4 libQtNetwork.so.4 libQtOpenGL.so.4 libQtSvg.so.4 libQtWebKit.so.4 libQtXml.so.4 libQtXmlPatterns.so.4
%define		boost_libs		libboost_date_time-.*.so.* libboost_filesystem-.*.so.* libboost_system-.*.so.* libboost_thread-.*.so.*
%define		ssl_libs		libcrypto.so.0.9.8 libssl.so.0.9.8
%define		phonon_libs		libphonon.so.4
%define		png_libs		libpng12.so.0
%define		pa_libs			libportaudio.so.2 libpulse-simple.so.0 libpulse.so.0
%define		vorbis_libs		libvorbis.so.0

# don't req libs provided by this package
%define		_noautoreq		%{libs1} %{libs2} %{qt_libs} %{boost_libs} %{ssl_libs} %{phonon_libs} %{png_libs} %{pa_libs} %{vorbis_libs}

%description
Guitar Pro is a musical software program offering all of the
functionalities that all guitarists need.

- Edit, visualize, and share your scores
- Learn to play or improve your technique
- Accompany yourself by creating the instrumental tracks of your
  choice
- Enjoy a series of essential tools: scale-validating tool, tuner,
  metronome, guitar fretboard...

%package data
Summary:	Guitar Pro data files
License:	GPL v2+
Group:		Applications/Multimedia
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description data
Guitar Pro data files.

%prep
%setup -qcT
ar xf %{SOURCE0}
tar xf data.tar.gz

mv opt/GuitarPro6 .
mv .%{_datadir}/{applications,pixmaps}/* .

%{__sed} -i -e '/^Exec=/ s#=/opt/GuitarPro6/launcher.sh#GuitarPro6#g' *.desktop

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_desktopdir},%{_pixmapsdir},%{_bindir}}
cp -l GuitarPro6.desktop $RPM_BUILD_ROOT/cp-test && l=l && rm -f $RPM_BUILD_ROOT/cp-test
cp -a$l GuitarPro6/* $RPM_BUILD_ROOT%{_appdir}
cp -p GuitarPro6.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p guitarpro6.png $RPM_BUILD_ROOT%{_pixmapsdir}
ln -s %{_appdir}/launcher.sh $RPM_BUILD_ROOT%{_bindir}/GuitarPro6

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/GuitarPro6
%{_desktopdir}/GuitarPro6.desktop
%{_pixmapsdir}/guitarpro6.png
%dir %{_appdir}
%{_appdir}/SoundbanksVolumeChangesSettings.ini
%attr(755,root,root) %{_appdir}/GPInstaller
%attr(755,root,root) %{_appdir}/GPUpdater
%attr(755,root,root) %{_appdir}/GuitarPro
%attr(755,root,root) %{_appdir}/launcher.sh

%attr(755,root,root) %{_appdir}/libGPCore.so
%attr(755,root,root) %{_appdir}/libOverLoud.so
%attr(755,root,root) %{_appdir}/libPickupModeling.so
%attr(755,root,root) %{_appdir}/libRSEAudioCore.so
%attr(755,root,root) %{_appdir}/libRSECore.so
%attr(755,root,root) %{_appdir}/libWavFile.so
%attr(755,root,root) %{_appdir}/libZip.so

%attr(755,root,root) %{_appdir}/libchunk.so
%attr(755,root,root) %{_appdir}/libexception.so
%attr(755,root,root) %{_appdir}/libfactory.so
%attr(755,root,root) %{_appdir}/libfilesystem.so
%attr(755,root,root) %{_appdir}/libmemory.so
%attr(755,root,root) %{_appdir}/libmmap.so
%attr(755,root,root) %{_appdir}/libobject.so
%attr(755,root,root) %{_appdir}/libprofiler.so
%attr(755,root,root) %{_appdir}/libregister.so
%attr(755,root,root) %{_appdir}/libthread.so
%attr(755,root,root) %{_appdir}/libtimer.so
%attr(755,root,root) %{_appdir}/libvariant.so
%attr(755,root,root) %{_appdir}/libxml.so

# phonon
%attr(755,root,root) %{_appdir}/libphonon.so.4

# qt4
%attr(755,root,root) %{_appdir}/libQtCore.so.4
%attr(755,root,root) %{_appdir}/libQtDBus.so.4
%attr(755,root,root) %{_appdir}/libQtGui.so.4
%attr(755,root,root) %{_appdir}/libQtNetwork.so.4
%attr(755,root,root) %{_appdir}/libQtOpenGL.so.4
%attr(755,root,root) %{_appdir}/libQtSvg.so.4
%attr(755,root,root) %{_appdir}/libQtWebKit.so.4
%attr(755,root,root) %{_appdir}/libQtXml.so.4
%attr(755,root,root) %{_appdir}/libQtXmlPatterns.so.4

# boost
%attr(755,root,root) %{_appdir}/libboost_date_time-*.so.*
%attr(755,root,root) %{_appdir}/libboost_filesystem-*.so.*
%attr(755,root,root) %{_appdir}/libboost_regex-*.so.*
%attr(755,root,root) %{_appdir}/libboost_system-*.so.*
%attr(755,root,root) %{_appdir}/libboost_thread-*.so.*

%files data
%defattr(644,root,root,755)
%{_appdir}/Data
%{_appdir}/Presets
%{_appdir}/updater
%{_appdir}/xsl
