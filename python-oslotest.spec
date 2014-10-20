# Created by pyp2rpm-1.1.1
%global pypi_name oslotest

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        OpenStack test framework

License:        ASL %(TODO: version)s
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx


%description
==========
 oslotest
==========

OpenStack test framework and test fixtures.

*
Free software: Apache license
* Documentation:
http://docs.openstack.org/developer/oslotest
* Source:
http://git.openstack.org/cgit/openstack/oslotest
* Bugs:
http://bugs.launchpad.net/oslo


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc html README.rst LICENSE
%{_bindir}/ 
%{_bindir}/oslo_debug_helper.sh
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/ 
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Oct 20 2014 Alan <apevec@gmail.com> - 1.1.0-1
- Initial package.