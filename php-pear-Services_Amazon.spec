%include	/usr/lib/rpm/macros.php
%define         _class          Services
%define         _subclass       Amazon
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - access to Amazon.com's web services
Summary(pl):	%{_pearname} - dost�p do serwis�w sieciowych Amazon.com
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bc168f666bcba86188cddb069c540cbf
URL:		http://pear.php.net/package/Services_Amazon/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Amazon uses Amazon.com's web services to allow developers to
search and provide associate links for specific ISBN numbers, authors,
artist, directors, and publishers among other things.

In PEAR status of this package is: %{_status}.

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
