from enum import Enum


class Result(Enum):
    Clean = 1
    Suspicious = 0
    NotDecided = -1


def unique(input: list) -> list:
  output = []
  for x in input:
    if not output or x != output[-1]:
      output.append(x)
  return output


class Robot:

    WHITE_LIST = list()

    @classmethod
    def run(cls, stack: str):
        dlls = stack.split(',')
        dlls = unique(dlls)
        result = cls.is_surrounded_by_whitelist(dlls)

        return result

    @classmethod
    def is_surrounded_by_whitelist(cls, dlls):
        na_indexes = [i for i, x in enumerate(dlls) if x == 'n/a']
        for index in na_indexes:
            if index:
                if dlls[index - 1] in cls.WHITE_LIST:
                    continue

            if index < len(dlls) - 1:
                if dlls[index + 1] in cls.WHITE_LIST:
                    continue

            return Result.NotDecided

        return Result.Clean


Robot.WHITE_LIST = ['1', '2', '3']
print(Robot.run('1,2,3,n/a,4,2,n/a,1'))
