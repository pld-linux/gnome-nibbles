Summary:	GNOME Nibbles - classic snake game
Summary(pl.UTF-8):	Nibbles dla GNOME - klasyczna gra w węża
Name:		gnome-nibbles
Version:	3.36.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-nibbles/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	ace2930d7d3df89e56436a6098e279dd
URL:		https://wiki.gnome.org/Apps/Nibbles
BuildRequires:	appstream-glib
BuildRequires:	clutter-devel >= 1.22.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	libgnome-games-support-devel >= 1
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson >= 0.44.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.28.0
BuildRequires:	vala-gsound >= 1.0.2
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	vala-libgnome-games-support >= 1
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	clutter >= 1.22.0
Requires:	clutter-gtk >= 1.4.0
Requires:	glib2 >= 1:2.40.0
Requires:	gsound >= 1.0.2
Requires:	gtk+3 >= 3.18.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 1:2.32.0
Provides:	gnome-games-gnibbles = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnibbles < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Nibbles is a game where the user controls a snake. The snake
moves around the board, eating diamonds while avoiding the walls
placed around it.

%description -l pl.UTF-8
GNOME Nibbles to gra, w której użytkownik steruje wężem. Wąż
przemieszcza się po planszy zjadając diamenty, unikając zderzeń ze
ścianami.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-nibbles
%{_datadir}/glib-2.0/schemas/org.gnome.nibbles.gschema.xml
%{_datadir}/gnome-nibbles
%{_datadir}/metainfo/org.gnome.Nibbles.appdata.xml
%{_desktopdir}/org.gnome.Nibbles.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Nibbles.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Nibbles.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Nibbles-symbolic.svg
%{_mandir}/man6/gnome-nibbles.6*
