class Parser:
    def __init__(self,separator,sub_separator) -> None:
        self.separator = separator
        self.sub_separator = sub_separator
    

    def __normalise_line_elements(self,elements: list[str]) -> tuple[str]:
        return tuple(map(lambda x : x.lower().strip(),elements))

    def __split_substitutes(self,*texts: str) -> tuple[str]:
        return [list(map(str.strip,text.split(self.sub_separator))) for text in texts]

    def parse(self,resource: list[str]):
        parsed_sets = []
        for i, line in enumerate(resource):
            # Skip commented lines
            if line.strip()[0] in ("#","/"):
                continue
            error_message = ""
            line_elements = line.split(self.separator)
            if len(line_elements) == 2:
                foreign_elements, local_elements = self.__normalise_line_elements(line_elements)
                if not foreign_elements or not local_elements:
                    error_message = "0 lenght definition"
                    continue
                foreign_elements, local_elements = self.__split_substitutes(foreign_elements,local_elements)
                parsed_sets.append((foreign_elements,local_elements))

            elif len(line_elements) == 1:
                error_message = "Insufficeint elements number"
            else:
                error_message = "Exceeded elements number"
            
            if error_message:
                print(f"Error occured while parsing in line number {i+1}: {error_message}")
        return parsed_sets

