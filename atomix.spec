%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Mind game - build molecules out of single atoms
Name:		atomix
Version:	44.0
Release:	1
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://triq.net/~jens/atomix.php
Source:		http://ftp.gnome.org/pub/gnome/sources/%{name}/%url_ver/%{name}-%{version}.tar.xz
#Patch0:		atomix-3.34.0-lto.patch

BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgnome-games-support-1)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils
BuildRequires:	meson
Requires(pre):	rpm-helper

%description
Atomix is a little mind game where you have to build molecules out of
single atoms. These are laying around between the walls and obstacles
on the playfield. Once you have pushed an atom in one direction it
moves until it hits an obstacle or another atom. It needs some thinking
how to construct complex molecules with this atom behaviour. The game
is inspired by the original Amiga version.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install

mkdir -p %{buildroot}/%{_localstatedir}/lib/games
touch %{buildroot}/%{_localstatedir}/lib/games/atomix.scores

%find_lang %{name}

%pre
%create_ghostfile %{_localstatedir}/lib/games/atomix.scores root games 0664


%files -f %{name}.lang
%doc README
%attr(2511, root, games) %{_bindir}/atomix
%{_datadir}/%{name}
%{_datadir}/icons/*/*/*/atomix*.*
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/*.desktop
%ghost %attr(0664,root,games) %{_localstatedir}/lib/games/atomix.scores
