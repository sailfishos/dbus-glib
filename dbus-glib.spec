Name:       dbus-glib
Summary:    GLib bindings for D-Bus
Version:    0.100.2
Release:    2
Group:      System/Libraries
License:    AFL/GPL
URL:        http://www.freedesktop.org/software/dbus/
Source0:    http://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libtool
BuildRequires:  expat-devel
BuildRequires:  gettext
BuildRequires:  autoconf

%description
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package devel
Summary:    Libraries and headers for the D-Bus GLib bindings
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Headers and static libraries for the D-Bus GLib bindings

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man page for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static \
    --disable-tests \
    --enable-verbose-mode=yes \
    --enable-asserts=yes \
    --disable-gtk-doc

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

gzip ChangeLog

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
	ChangeLog.gz NEWS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*glib*.so.*
%{_bindir}/dbus-binding-tool
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
/usr/libexec/dbus-bash-completion-helper

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_includedir}/dbus-1.0/dbus/*

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}
%doc %{_datadir}/gtk-doc/html/dbus-glib
