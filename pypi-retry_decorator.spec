#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-retry_decorator
Version  : 1.1.1
Release  : 50
URL      : https://files.pythonhosted.org/packages/6e/e6/bedc75b264cbcbf6e6d0e5071d96d739f540fc09be31744a7a8824c02a8e/retry_decorator-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/e6/bedc75b264cbcbf6e6d0e5071d96d739f540fc09be31744a7a8824c02a8e/retry_decorator-1.1.1.tar.gz
Summary  : Retry Decorator
Group    : Development/Tools
License  : MIT
Requires: pypi-retry_decorator-license = %{version}-%{release}
Requires: pypi-retry_decorator-python = %{version}-%{release}
Requires: pypi-retry_decorator-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://badge.fury.io/py/retry_decorator.svg
:target: https://badge.fury.io/py/retry_decorator

%package license
Summary: license components for the pypi-retry_decorator package.
Group: Default

%description license
license components for the pypi-retry_decorator package.


%package python
Summary: python components for the pypi-retry_decorator package.
Group: Default
Requires: pypi-retry_decorator-python3 = %{version}-%{release}

%description python
python components for the pypi-retry_decorator package.


%package python3
Summary: python3 components for the pypi-retry_decorator package.
Group: Default
Requires: python3-core
Provides: pypi(retry_decorator)

%description python3
python3 components for the pypi-retry_decorator package.


%prep
%setup -q -n retry_decorator-1.1.1
cd %{_builddir}/retry_decorator-1.1.1
pushd ..
cp -a retry_decorator-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404932
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-retry_decorator
cp %{_builddir}/retry_decorator-1.1.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retry_decorator/4a87a559be6eb9023bf0b0e3bd37a71f7b6d1f9e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-retry_decorator/4a87a559be6eb9023bf0b0e3bd37a71f7b6d1f9e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
