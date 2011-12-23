%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-dtopt
Summary:        Add options to doctest examples while they are running
Version:        0.1
Release:        6%{?dist}
License:        MIT
Group:          System Environment/Libraries
URL:            http://pypi.python.org/pypi/dtopt/
Source0:        http://pypi.python.org/packages/source/d/dtopt/dtopt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-setuptools-devel

%description
dtopts adds options to doctest examples while they are running. When
using the doctest module it is often convenient to use the ELLIPSIS
option, which allows you to use ... as a wildcard. But you either have
to setup the test runner to use this option, or you must put #doctest:
+ELLIPSIS on every example that uses this feature. dtopt lets you enable
this option globally from within a doctest, by doing: 
>>> from dtopt import ELLIPSIS

%prep
%setup -q -n dtopt-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/dtopt/
%{python_sitelib}/dtopt*.egg-info/

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.1-5
- Change define to global.
- Remove unnecessary BuildRequires on python-devel.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-3
- Rebuild for Python 2.6

* Fri Jun 27 2008 Ricky Zhou <ricky@fedoraproject.org> 0.1-2
- Initial package for Fedora

* Sat Mar 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-1
- Initial package for Fedora
