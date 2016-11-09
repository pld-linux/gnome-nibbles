Summary:	GNOME Nibbles - classic snake game
Summary(pl.UTF-8):	Nibbles dla GNOME - klasyczna gra w węża
Name:		gnome-nibbles
Version:	3.22.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-nibbles/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	c292366edef1773fc1676bad73a4df04
URL:		https://wiki.gnome.org/Apps/Nibbles
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.22.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	intltool >= 0.50.2
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgnome-games-support-devel >= 1
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.28.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	clutter >= 1.22.0
Requires:	clutter-gtk >= 1.4.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.18.0
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
%{__aclocal} -I m4
%{__autoconf}
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
%{_datadir}/appdata/org.gnome.Nibbles.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.nibbles.gschema.xml
%{_datadir}/gnome-nibbles
%{_desktopdir}/org.gnome.Nibbles.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-nibbles.png
%{_iconsdir}/hicolor/scalable/apps/gnome-nibbles.svg
%{_iconsdir}/hicolor/symbolic/apps/gnome-nibbles-symbolic.svg
%{_mandir}/man6/gnome-nibbles.6*
