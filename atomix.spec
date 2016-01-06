%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Mind game - build molecules out of single atoms
Name:		atomix
Version:	3.18.0
Release:	1
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://triq.net/~jens/atomix.php
Source:		http://ftp.gnome.org/pub/gnome/sources/%{name}/%url_ver/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils
Requires(pre):	rpm-helper

%description
Atomix is a little mind game where you have to build molecules out of
single atoms. These are laying around between the walls and obstacles
on the playfield. Once you have pushed an atom in one direction it
moves until it hits an obstacle or another atom. It needs some thinking
how to construct complex molecules with this atom behaviour. The game
is inspired by the original Amiga version.

%prep
%setup -q

%build
export LDFLAGS="${LDFLAGS} -lm" 
%configure --bindir=%{_gamesbindir} --localstatedir=%{_localstatedir}/lib

%make

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std \
	bindir=%{_gamesbindir} \
	localstatedir=%{_localstatedir}/lib

mkdir -p %{buildroot}/%{_localstatedir}/lib/games
touch %{buildroot}/%{_localstatedir}/lib/games/atomix.scores

%find_lang %{name}

%pre
%create_ghostfile %{_localstatedir}/lib/games/atomix.scores root games 0664


%files -f %{name}.lang
%doc README
%attr(2511, root, games) %{_gamesbindir}/atomix
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%ghost %{_localstatedir}/lib/games/atomix.scores

