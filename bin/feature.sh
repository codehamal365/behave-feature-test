#!/bin/bash
set -e

mkdir -p build/

# shellcheck disable=SC2089

shopt -s nocasematch

options=''
if [[ "${NIGHTLY}" != "True" && "${PULL_REQUEST}" != "True" ]]
then
  options="${options} --tags=~@nightly"
else
  options="${options} --no-skipped"
fi

if [ ! -z ${feature+x} ]
then
  options="${options} features/${feature}.feature"
fi

if [ ! -z ${scenario+x} ]
then
  options="${options} --name '^${scenario}\$'"
fi

command="behave \
  --junit --junit-directory build/behave-report \
  --format pretty \
  --tags=~@skip \
  --tags=~@manual \
  ${options} "

for argument in "$@"
do
  command=${command}" '${argument}'"
done

./dev bash -c "${command}"