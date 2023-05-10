%global sname tldextract
%global owner john-kurkowski

Name:       python-%{sname}
Version:    3.4.1
Release:    1%{?dist}
Summary:    Python library for parsing domains
License:    BSD
URL:        https://github.com/%{owner}/%{sname}
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz#/%{sname}-%{version}.tar.gz
BuildArch:  noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel python3-pytest python3-responses
Requires:       python3

%description
tldextract accurately separates a URL's subdomain, domain, and public suffix
using the Public Suffix List (PSL).

%package -n python3-%{sname}
Summary:    %{summary}

%description -n python3-%{sname}
tldextract accurately separates a URL's subdomain, domain, and public suffix
using the Public Suffix List (PSL).

%prep
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%autosetup -p1 -n %{sname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{sname}

%check
%pytest -k "not cache"

%files -n python3-%{sname} -f %{pyproject_files}
%doc README.md
/usr/bin/tldextract

%changelog
* Wed May 10 2023 Italo Garcia <italo.garcia@aiven.io> - 3.4.1-1
- Initial package
