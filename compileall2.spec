#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compileall2
Version  : 20.03.03
Release  : 2
URL      : file:///insilications/build/clearlinux/packages/compileall2/compileall2-.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/compileall2/compileall2-.tar.gz
Summary  : Enhanced Python `compileall` module
Group    : Development/Tools
License  : MIT
Requires: compileall2-bin = %{version}-%{release}
Requires: compileall2-python = %{version}-%{release}
Requires: compileall2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# compileall2 Python module
Copy of `compileall` module from CPython source code with some new features, namely:

%package bin
Summary: bin components for the compileall2 package.
Group: Binaries

%description bin
bin components for the compileall2 package.


%package python
Summary: python components for the compileall2 package.
Group: Default
Requires: compileall2-python3 = %{version}-%{release}

%description python
python components for the compileall2 package.


%package python3
Summary: python3 components for the compileall2 package.
Group: Default
Requires: python3-core
Provides: pypi(compileall2)

%description python3
python3 components for the compileall2 package.


%prep
%setup -q -n compileall2
cd %{_builddir}/compileall2

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610387056
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/compileall2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
