Summary:	GNOME Nibbles - classic snake game
Summary(pl.UTF-8):	Nibbles dla GNOME - klasyczna gra w węża
Name:		gnome-nibbles
Version:	3.18.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-nibbles/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	e4adb6cfdd55b60e9aeecad978bc5257
URL:		https://wiki.gnome.org/Apps/Nibbles
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.14.4
BuildRequires:	clutter-gtk-devel >= 1.2.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	intltool >= 0.50
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter >= 1.14.4
Requires:	clutter-gtk >= 1.2.0
Requires:	gtk+3 >= 3.15.0
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/appdata/gnome-nibbles.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.nibbles.gschema.xml
%{_datadir}/gnome-nibbles
%{_desktopdir}/gnome-nibbles.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-nibbles.png
%{_iconsdir}/hicolor/scalable/apps/gnome-nibbles.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-nibbles-symbolic.svg
%{_mandir}/man6/gnome-nibbles.6*
