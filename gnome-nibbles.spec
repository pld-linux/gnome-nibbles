# TODO: use gtk4-update-icon-cache
Summary:	GNOME Nibbles - classic snake game
Summary(pl.UTF-8):	Nibbles dla GNOME - klasyczna gra w węża
Name:		gnome-nibbles
Version:	4.0.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-nibbles/4.0/%{name}-%{version}.tar.xz
# Source0-md5:	c000d7db2943f506e88653637719aa73
URL:		https://wiki.gnome.org/Apps/Nibbles
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk4-devel >= 4.6
BuildRequires:	libgnome-games-support2-devel >= 2.0.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson >= 0.62
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.10
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.44
BuildRequires:	vala-gsound >= 1.0.2
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	vala-libgnome-games-support2 >= 2.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.66.0
Requires:	glib2 >= 1:2.66.0
Requires:	gsound >= 1.0.2
Requires:	gtk4 >= 4.6
Requires:	hicolor-icon-theme
Requires:	libgnome-games-support2 >= 2.0.0
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
%{_datadir}/dbus-1/services/org.gnome.Nibbles.service
%{_datadir}/glib-2.0/schemas/org.gnome.Nibbles.gschema.xml
%{_datadir}/gnome-nibbles
%{_datadir}/metainfo/org.gnome.Nibbles.appdata.xml
%{_desktopdir}/org.gnome.Nibbles.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Nibbles.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Nibbles-symbolic.svg
%{_mandir}/man6/gnome-nibbles.6*
