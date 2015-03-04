Summary:	Music AcoustID fingerprinting application
Name:		acoustid-fingerprinter
Version:	0.6
Release:	4
Group:		Sound
License:	GPLv2+
Url:		http://acoustid.org/fingerprinter
Source0:	https://bitbucket.org/acoustid/acoustid-fingerprinter/downloads/%{name}-%{version}.tar.gz
Patch0:		acoustid-fingerprinter-request-s16-audio-format.patch
Patch1:		acoustid-fingerprinter-0.6-ffmpeg-2.0.patch
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	qt4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libchromaprint)

%description
Acoustid fingerprinter is a cross-platform GUI application that uses
Chromaprint to submit audio fingerprints from your music collection 
to the Acoustid database. Only tagged audio files are submitted. 
Files tagged by MusicBrainz applications such as Picard are preferred,
but it will submit fingerprints for any files that have tags such as
track title, artist name, album name, etc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

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

