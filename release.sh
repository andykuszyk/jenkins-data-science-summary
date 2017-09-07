old_version=$1
new_version=$2
sed -i -e "s/$old_version/$new_version/g" setup.py
git commit -am "Updated to version $new_version"
git tag $new_version
git push
git push origin --tags