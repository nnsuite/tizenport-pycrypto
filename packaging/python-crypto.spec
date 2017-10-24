Name:     python-crypto
Summary:  Cryptography library for Python
Version:  2.7.1
Release:  0
License:  Public Domain and Python
URL:      https://github.com/dlitz/pycrypto
Source0:  %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires: python-devel
BuildRequires: python >= 2.2
Requires: python >= 2.2

%description
pycrypto is a collection of cryptographic algorithms and protocols,
implemented for use from Python.

%prep
%setup -q
cp %{SOURCE1001} .

%build
/usr/bin/python2 setup.py build

%install
/usr/bin/python2 setup.py install --prefix=%{_prefix} --install-lib=%{python_sitelib} --root=%{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*
