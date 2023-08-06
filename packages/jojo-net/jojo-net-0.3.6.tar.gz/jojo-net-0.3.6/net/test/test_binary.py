from net.binary import *
import unittest


class TestBinary(unittest.TestCase):
    def test_init(self):
        p = Binary()
        self.assertEqual(p.size, 0)
        self.assertEqual(p.capacity, 0)

        bs = b'abc'
        p = Binary(bs)
        p2 = Binary(p)
        p3 = Binary(p2)
        self.assertEqual(p.to_hex(), p.to_hex())
        self.assertEqual(p3.to_hex(), p.to_hex())

    def read_write_string(self, file=None, endian='little'):
        s = "Hello"
        ss = "Baby"

        if isinstance(file, str):
            mode_write = 'wb+'
            mode_read = 'rb'
        else:
            mode_read = mode_write = None

        data = file

        # write_string
        p = Binary(data, mode_write, endian=endian)
        p.write_string(s)
        p.write_string(ss)
        p.close()

        data = p if file is None else file

        # read_string
        p = Binary(data, mode_read, endian=endian)
        p.offset = 0
        s2 = p.read_string()
        ss2 = p.read_string()
        self.assertEqual(s, s2)
        self.assertEqual(ss, ss2)
        p.close()

    def read_write_bytes(self, file=None, endian='little'):
        s = b"abc"
        ss = b"def"

        if isinstance(file, str):
            mode_write = 'wb+'
            mode_read = 'rb'
        else:
            mode_read = mode_write = None

        data = file

        # write_string
        p = Binary(data, mode_write, endian=endian)
        p.write_bytes(s)
        p.write_bytes(ss)
        p.close()

        data = p if file is None else file

        # read_string
        p = Binary(data, mode_read, endian=endian)
        p.offset = 0
        s2 = p.read_bytes(3)
        ss2 = p.read_bytes(3)
        self.assertEqual(s, s2)
        self.assertEqual(ss, ss2)
        p.close()

    def read_write_int(self, file=None, endian='little'):
        if isinstance(file, str):
            mode_write = 'wb+'
            mode_read = 'rb'
        else:
            mode_read = mode_write = None

        # test put_int8 and get_int8
        data = file
        for i in range(-127, 128):
            n = i
            p = Binary(data, mode_write, endian=endian)
            p.put_int8(n, 0)
            p.close()

            data = p if file is None else file

            p = Binary(data, mode_read, endian=endian)
            n2 = p.get_int8(0)
            self.assertEqual(n, n2)

        # test put_int16 and get_int16
        data = file
        for i in range(-32767, 32767, 0xFF):
            n = i
            p = Binary(data, mode_write, endian=endian)
            p.put_int16(n, 0)
            p.close()

            data = p if file is None else file

            p = Binary(data, mode_read, endian=endian)
            n2 = p.get_int16(0)
            self.assertEqual(n, n2)

        # test put_int32 and get_int32
        data = file
        for i in range(-0x7FFFFF, 0x7FFFFF, 0xFFEF):
            n = i
            p = Binary(data, mode_write, endian=endian)
            p.put_int32(n, 0)
            p.close()

            data = p if file is None else file

            p = Binary(data, mode_read, endian=endian)
            n2 = p.get_int32(0)
            self.assertEqual(n, n2)

        # test put_int64 and get_int64
        data = file
        for i in range(-0x7FFFFF, 0x7FFFFF, 0xFFEF):
            n = i
            p = Binary(data, mode_write, endian=endian)
            p.put_int64(n, 0)
            p.close()

            data = p if file is None else file

            p = Binary(data, mode_read, endian=endian)
            n2 = p.get_int64(0)
            self.assertEqual(n, n2)

    def read_write_domain_name(self, file=None, endian='little'):
        name = "www.baidu.com"

        if isinstance(file, str):
            mode_write = 'wb+'
            mode_read = 'rb'
        else:
            mode_read = mode_write = None

        data = file

        # write_string
        p = Binary(data, mode_write, endian=endian)
        p.write_domain_name(name)
        p.close()

        data = p if file is None else file

        # read_string
        p = Binary(data, mode_read, endian=endian)
        p.offset = 0
        name2 = p.read_domain_name()
        p.close()
        self.assertEqual(name, name2)

    def t1est_read_write(self):
        self.read_write_domain_name()
        self.read_write_domain_name('1.dat')

        self.read_write_bytes()
        self.read_write_string(endian="little")
        self.read_write_string(endian="big")
        self.read_write_int(endian="little")
        self.read_write_int(endian="big")

        self.read_write_bytes('1.dat')
        self.read_write_string('1.dat', endian="little")
        self.read_write_string('1.dat', endian="big")
        self.read_write_int('1.dat', endian="little")
        self.read_write_int('1.dat', endian="big")


class TestField(unittest.TestCase):
    def test_basic(self):
        name = "Peter"
        age = 18
        sex = 1
        salary = 300.3
        domain = "www.baidu.com"

        data = Binary()
        data.write_string(name)
        data.write_int16(age)
        data.write_byte(sex)
        data.write_float64(salary)
        data.write_domain_name(domain)

        field_name = String()
        field_age = Int16()
        field_sex = Uint8()
        field_salary = Float64()
        field_domain = DomainName()

        offset = 0
        offset, _ = field_name.read_binary(data, offset)
        offset, _ = field_age.read_binary(data, offset)
        offset, _ = field_sex.read_binary(data, offset)
        offset, _ = field_salary.read_binary(data, offset)
        offset, _ = field_domain.read_binary(data, offset)

        self.assertEqual(age, field_age._value)
        self.assertEqual(name, field_name.value)
        self.assertEqual(sex, field_sex._value)
        self.assertEqual(salary, round(field_salary._value, 4))
        self.assertEqual(domain, field_domain.value)

    def test_float(self):
        f = -3.3323
        d = -4.41232467

        data = Binary()
        data.write_float32(f)
        data.write_float64(d)
        self.assertEqual(data.capacity, 12)

        data.offset = 0
        f2 = data.read_float32()
        d2 = data.read_float64()

        self.assertEqual(f, round(f2, 6))
        self.assertEqual(d, round(d2, 12))

    def test_default_value(self):
        self.assertEqual(Bit1().value, 0)
        self.assertEqual(Bit3().value, 0)
        self.assertEqual(Int8().value, 0)
        self.assertEqual(Uint16().value, 0)
        self.assertEqual(Float32().value, 0)
        self.assertEqual(Pointer32().value, 0)
        self.assertEqual(String().value, '')
        self.assertEqual(DomainName().value, '')

    def test_byte_array(self):
        data = Binary()
        f = Array(10)
        f.value = bytearray(b'\0\1')
        f.write_binary(data, 0)
        self.assertEqual(data.capacity, 10)


class Student(Structure):
    id = Uint32
    name = String
    age = Int16
    sex = Uint8
    score = Float64
    data_len = Uint8
    data = Array('data_len')
    domain = DomainName


class Person(Structure):
    name = String
    age = Int16


class School(Structure):
    count = Int16
    persons = Array(Person, 'count')


class ArrayInt(Structure):
    data = Array(Int16)


class ArrayString(Structure):
    data = Array(String)


class TestStructure(unittest.TestCase):
    def test_basic(self):
        peter = Student()
        peter.id = 12345678
        peter.name = "Peter"
        peter.age = 18
        peter.sex = 1
        peter.score = 83.5
        peter.data_len = 3
        peter.data = bytearray(b'\01\02\03')  # + b'\0' * 7
        peter.domain = "www.baidu.com"

        data = Binary()
        peter.write_binary(data)

        stu = Student(data)
        self.assertEqual(peter.id, stu.id)
        self.assertEqual(peter.name, stu.name)
        self.assertEqual(peter.age, stu.age)
        self.assertEqual(peter.sex, stu.sex)
        self.assertEqual(peter.score, stu.score)
        self.assertEqual(peter.data_len, stu.data_len)
        self.assertEqual(peter.data, stu.data)
        self.assertEqual(peter.domain, stu.domain)
        self.assertEqual(len(stu.data), stu.data_len)

        stu = Student(peter)
        self.assertEqual(peter.id, stu.id)
        self.assertEqual(peter.name, stu.name)
        self.assertEqual(peter.age, stu.age)
        self.assertEqual(peter.sex, stu.sex)
        self.assertEqual(peter.score, stu.score)
        self.assertEqual(peter.data, stu.data)
        self.assertEqual(peter.domain, stu.domain)

        d = stu.to_dict()
        self.assertEqual(peter.id, d['id'])
        self.assertEqual(peter.name, d['name'])
        self.assertEqual(peter.age, d['age'])
        self.assertEqual(peter.sex, d['sex'])
        self.assertEqual(peter.score, d['score'])
        self.assertEqual(peter.data_len, d['data_len'])
        self.assertEqual(peter.data, d['data'])
        self.assertEqual(peter.domain, d['domain'])

        stu = Student(d)
        self.assertEqual(peter.id, stu.id)
        self.assertEqual(peter.name, stu.name)
        self.assertEqual(peter.age, stu.age)
        self.assertEqual(peter.sex, stu.sex)
        self.assertEqual(peter.score, stu.score)
        self.assertEqual(peter.data_len, stu.data_len)
        self.assertEqual(peter.data, stu.data)
        self.assertEqual(peter.domain, stu.domain)

    def test_array(self):
        t = ArrayString()
        t.data = ["hello", "world"]

        t = ArrayInt()
        t.data = [3, 5]
        self.assertEqual(t.to_bytes(), b'\00\03\00\05')

        data = Binary(endian='little')
        t.write_binary(data)
        self.assertEqual(data.to_bytes(), b'\03\00\05\00')

    def test_array_of_structure(self):
        p1 = Person({'name': 'Peter', 'age': 33})
        p2 = Person({'name': 'Sam', 'age': 19})
        school = School()
        school.persons = [p1, p2, {'name': 'Mary', 'age': 22}]
        school.count = len(school.persons)
        data = Binary('1.dat')
        school.write_binary(data)
        bs = data.to_bytes()

        s2 = School('1.dat')

    def test_new_class(self):
        NewClass = new_class({
            "name": String,
            "age": Int16
        })

        a = NewClass()
        a.name = "Mary"
        a.age = 28


if __name__ == "__main__":
    unittest.main()
