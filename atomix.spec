%define	version	2.14.0
%define release	7

Summary:		Mind game - build molecules out of single atoms
Name:		atomix
Version:		%{version}
Release:		%{release}
License:		GPLv2+
Group:		Games/Puzzles
URL:		http://triq.net/~jens/atomix.php
Source:		ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:		atomix-zh_TW.po.bz2

BuildRequires:	pkgconfig(libgnomeui-2.0)
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
export LDFLAGS="${LDFLAGS} -lm" 
%configure --bindir=%{_gamesbindir} --localstatedir=%{_localstatedir}/lib
# fix localization
sed  -i 's!^SOURCES = !&\n'"$(grep "^CATALOGS" po/Makefile.in)"'!' po/Makefile

%make

%install
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


%files -f %{name}.lang
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





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.14.0-7mdv2011.0
+ Revision: 616630
- the mass rebuild of 2010.0 packages

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 2.14.0-6mdv2010.0
+ Revision: 384167
- fix install (localstatedir to /var/lib)
- fix license

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 2.14.0-3mdv2008.1
+ Revision: 187660
- rebuild for 2008.1

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Sep 18 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-09-17 06:08:29 (61766)
- atomix-2.14.0-2mdv2007.0

* Sun Sep 17 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-09-16 17:02:56 (61764)
- Remove wrong category

* Sun Sep 17 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-09-16 16:58:06 (61763)
- XDG

* Fri Aug 04 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 03:43:31 (43086)
- import atomix-2.14.0-1mdk

* Sat Apr 29 2006 Jerome Soyer <saispo@mandriva.org> 2.14.0-1mdk
- New release 2.14.0
- Fix Url

* Wed Nov 16 2005 Abel Cheung <deaddog@mandriva.org> 1.2.4-1mdk
- New release 1.2.4

* Fri Sep 09 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.2.2a-2mdk
- Fix BuildRequires  ( because of the use of convert )
- mkrel

* Mon Aug 08 2005 Abel Cheung <deaddog@mandriva.org> 1.2.2a-1mdk
- New release
- Drop my icons, use official one
- Update traditional Chinese translation

* Tue Jun 21 2005 Abel Cheung <deaddog@mandriva.org> 1.2.1-1mdk
- New version (nice to know it's risen from coffin)
- Drop patch (not needed)

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 1.0.1-3mdk
- Yet another BuildRequires fix
- Fix pre script

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 1.0.1-2mdk
- Fix BuildRequires (thx Stefan's bot)
- P0: fix build with newer gcc
- Regen auto* stuff because of change in intltool

* Wed Dec 31 2003 Abel Cheung <deaddog@deaddog.org> 1.0.1-1mdk
- First Mandrake package (?)

