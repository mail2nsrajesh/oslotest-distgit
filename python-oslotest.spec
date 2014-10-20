# Created by pyp2rpm-1.1.1
%global pypi_name oslotest

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        OpenStack test framework

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx


%description
OpenStack test framework and test fixtures.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

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
* Mon Oct 20 2014 Alan Pevec <apevec@redhat.com> - 1.1.0-1
- Initial package.
