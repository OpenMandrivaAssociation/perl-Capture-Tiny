
%define realname   Capture-Tiny
%define version    0.05
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Capture STDOUT and STDERR from Perl, XS or external programs
Source:     http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
Capture::Tiny provides a simple, portable way to capture anything sent to
STDOUT or STDERR, regardless of whether it comes from Perl, from XS code or
from an external program. Optionally, output can be teed so that it is
captured while being passed through to the original handles. Yes, it even
works on Windows. Stop guessing which of a dozen capturing modules to use
in any particular situation and just use this one.

This module was heavily inspired by the IO::CaptureOutput manpage, which
provides similar functionality without the ability to tee output and with
more complicated code and API.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


