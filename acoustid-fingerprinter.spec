Name:           acoustid-fingerprinter
Version:        0.5.1
Release:        %mkrel 1
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


