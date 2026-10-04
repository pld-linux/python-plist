Summary:	Python 2 bindings for libplist
Summary(pl.UTF-8):	Wiązania libplist dla Pythona 2
Name:		python-plist
Version:	2.4.0
Release:	6
License:	LGPL v2.1+
Group:		Development/Languages/Python
# Source0Download: https://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libplist/releases/download/%{version}/libplist-%{version}.tar.bz2
# Source0-md5:	56b7892151b72ea0cfbf3ef785ffbc82
Patch0:		libplist-sh.patch
Patch1:		libplist-link.patch
Patch2:		libplist-system-library.patch
URL:		https://libimobiledevice.org/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libplist-devel >= 2.4.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	python-Cython >= 0.17.0
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpm-pythonprov
Requires:	libplist >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libplist.

%description -l pl.UTF-8
Wiązania libplist dla Pythona 2.

%prep
%setup -q -n libplist-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

touch cython/*.py[xh]

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_path_CYTHON=/usr/bin/cython2 \
	PYTHON=%{__python} \
	--disable-silent-rules \
	--disable-static \
	--without-tests

%{__make} -C cython

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C cython install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/plist.la
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%{py_sitedir}/plist.so
