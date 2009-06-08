%define	version	2.14.0
%define release	%mkrel 6

Summary:	Mind game - build molecules out of single atoms
Name:		atomix
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://triq.net/~jens/atomix.php
Source:		ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	atomix-zh_TW.po.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnomeui2-devel
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

[ "%{version}" = "1.2.2a" ] && bzip2 -dc %{SOURCE1} > po/zh_TW.po

%build
%configure2_5x --bindir=%{_gamesbindir} --localstatedir=%{_localstatedir}/lib
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std \
	bindir=%{_gamesbindir} \
	localstatedir=%{_localstatedir}/lib


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="PuzzleGame" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Puzzles" \
  --add-category="Game" \
  --add-category="LogicGame" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}%{_miconsdir} \
         %{buildroot}%{_iconsdir} \
         %{buildroot}%{_liconsdir}
convert -geometry 16x16 atomix-icon.png %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644       atomix-icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 48x48 atomix-icon.png %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

%pre
%create_ghostfile %{_localstatedir}/lib/games/atomix.scores root games 0664

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%attr(2511, root, games) %{_gamesbindir}/atomix
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/*.png
%ghost %{_localstatedir}/lib/games/atomix.scores

%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png



