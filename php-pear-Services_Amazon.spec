%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Amazon
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - access to Amazon.com's web services
Summary(pl):	%{_pearname} - dostêp do us³ug sieciowych Amazon.com
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f7aa4127fe59cefc6d2a3abc1e4e02b9
URL:		http://pear.php.net/package/Services_Amazon/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Client
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Serializer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Amazon uses Amazon.com's web services to allow developers to
search and provide associate links for specific ISBN numbers, authors,
artist, directors, and publishers among other things.

In PEAR status of this package is: %{_status}.

%description -l pl
Services_Amazon za pomoc± us³ug sieciowych Amazon.com pozwala
deweloperom na wyszukiwanie i dostarczanie adresów m.in. dla
konkretnych numerów ISBN, autorów, artystów, re¿yserów czy wydawców.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
