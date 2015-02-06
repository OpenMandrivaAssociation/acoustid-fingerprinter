Name:           acoustid-fingerprinter
Version:        0.5.1
Release:        2
Summary:        Music AcoustID fingerprinting application

Group:          Sound
License:        GPLv2+
URL:            http://acoustid.org/fingerprinter
Source:         https://github.com/downloads/lalinsky/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %_tmppath/%name-%version-%release-buildroot
BuildRequires:  cmake
BuildRequires:  qt4-devel
%if %mdvver > 201100
BuildRequires:  ffmpeg0.7-devel
%else
BuildRequires:  ffmpeg-devel
%endif
BuildRequires:  taglib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libchromaprint)


%description

Acoustid fingerprinter is a cross-platform GUI application that uses
Chromaprint to submit audio fingerprints from your music collection 
to the Acoustid database. Only tagged audio files are submitted. 
Files tagged by MusicBrainz applications such as Picard are preferred,
but it will submit fingerprints for any files that have tags such as
track title, artist name, album name, etc.

%prep
%setup -q


%build
%cmake -DCMAKE_BUILD_TYPE=Debug
# removing the -O3 optimization flag for the release building type
sed -i  "s/-O3 -DNDEBUG//g" CMakeCache.txt
%make


%install
rm -rf %buildroot
cd build
%makeinstall_std
cd ..

install -d -m755 %{buildroot}%{_datadir}/applications

desktop-file-install \
  --remove-key Encoding \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

install -p -D -m 0644 images/%{name}.svg  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%doc CHANGES.txt COPYING.txt 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg




%changelog
* Mon Jun 11 2012 Götz Waschk <waschk@mandriva.org> 0.5.1-1
+ Revision: 804387
- import acoustid-fingerprinter


* Mon Jun 11 2012 Goetz Waschk <goetz@mandriva.org> 0.5.1-1
- adapt for Mandriva

* Wed May 9 2012 Ismael Olea <ismael@olea.org> - 0.5.1-5
- bump

* Wed Apr 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-4
- Rebuilt

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-3
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-2
- Rebuilt for x264/FFmpeg

* Sat Jan 14 2012 Ismael Olea <ismael@olea.org> - 0.5.1-1
- updated to 0.5.1
- desktop svg icon now provided upstream
- fix-contenttypeheader.patch included in upstream
- Now CMAKE configured for Debug release -> better debuginfo
- added update-mime-database scriptlets

* Wed Jan 4 2012 Ismael Olea <ismael@olea.org> - 0.5-2
- upstream now includes desktop file
- patch0 fixes https://github.com/lalinsky/acoustid-fingerprinter/issues/3
- removing the -O3 optimization flag for the release building type
- more spec cleaning

* Sun Jan 1 2012 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- minor spec cleaning

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.4-1
- first version for Fedora

