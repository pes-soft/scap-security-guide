
# IMPORTANT NOTE: This spec file is solely dedicated to make changes to the
# Fedora's scap-security-guide package. If you want to apply changes against
# the main RHEL-6 scap-security-guide RPM content, use scap-security-guide.spec
# file one level up - in the main scap-security-guide directory (instead of
# this one).

%global	fedorassgrelease	3.rc1

Name:		scap-security-guide
Version:	0.1
Release:	%{fedorassgrelease}%{?dist}
Summary:	Security guidance and baselines in SCAP formats
Group:		Applications/System
License:	Public Domain
URL:		https://fedorahosted.org/scap-security-guide/
Source0:	http://fedorapeople.org/~jlieskov/%{name}-%{version}-%{fedorassgrelease}.tar.gz
BuildArch:	noarch
BuildRequires:	libxslt, expat, python, openscap-utils >= 0.9.1, python-lxml
Requires:	openscap-utils >= 0.9.1

%description
The scap-security-guide project provides guide for configuration of the
system from final system's security point of view. The guidance is specified
in the Security Content Automation Protocol (SCAP) format and consitutes
a catalog of practical hardening advice linked to government requirements
where applicable. The project bridges the gap between generalized policy
requirements and specific implementation guidelines.

%prep
%setup -q -n %{name}-%{version}-%{fedorassgrelease}

%build
cd Fedora && make dist

%install
mkdir -p %{buildroot}%{_datadir}/xml/scap/ssg/fedora
mkdir -p %{buildroot}%{_mandir}/en/man8/

# Add in core content (SCAP, guide)
cp -a Fedora/dist/* %{buildroot}%{_datadir}/xml/scap/ssg/fedora

# Add in manpage
cp -a Fedora/input/auxiliary/scap-security-guide.8 %{buildroot}%{_mandir}/en/man8/scap-security-guide.8

%files
%{_datadir}/xml/scap/ssg/fedora/*
%lang(en) %{_mandir}/en/man8/scap-security-guide.8.*
%doc Fedora/LICENSE

%changelog
* Tue Oct 15 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-3.rc1
- Fixes for scap-security-guide Fedora RPM review request (RH BZ#1018905):
  * drop Fedora release from package provided files' final path (c#5),
  * drop BuildRoot, selected Requires:, clean section, drop chcon for
    manual page, don't gzip man page (c#4),
  * change package's description (c#4),
  * include PD license text (#c4).

* Mon Oct 14 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-2
- Provide manual page for scap-security-guide
- Remove percent sign from spec's changelog to silence rpmlint warning
- Convert RHEL6 'Restrict Root Logins' section's rules to Fedora
- Convert RHEL6 'Set Password Expiration Parameter' rules to Fedora
- Introduce 'Account and Access Control' section
- Convert RHEL6 'Verify Proper Storage and Existence of Password Hashes' section's
  rules to Fedora
- Set proper name of the build directory in the spec's setup macro.
- Replace hard-coded paths with macros. Preserve attributes when copying files.

* Tue Sep 17 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-1
- Initial Fedora SSG RPM.
